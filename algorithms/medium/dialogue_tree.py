"""
Алгоритм (Medium): Дерево диалогов.

Представляет структуру диалога в виде дерева решений.
Поддерживает:
- Построение из списка диалогов
- Рекурсивный обход (DFS)
- Поиск всех концовок
- Поиск пути между узлами (BFS)
- Визуализацию структуры
"""


class DialogueNode:
    """Узел дерева диалогов."""
    
    def __init__(self, index, dialogue_type, data=None):
        self.index = index
        self.dialogue_type = dialogue_type
        self.data = data or {}
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def is_ending(self):
        return "next_scene" in self.data
    
    def get_text(self):
        if "text" in self.data:
            speaker = self.data.get("speaker", "")
            text = self.data["text"]
            return f"{speaker}: {text}" if speaker else text
        return f"[{self.dialogue_type}]"
    
    def __repr__(self):
        return f"Node({self.index}, {self.dialogue_type})"


class DialogueTree:
    """Дерево диалогов с алгоритмами обхода."""
    
    def __init__(self):
        self.nodes = {}
        self.root = None
    
    def build_from_dialogues(self, dialogues):
        """Строит дерево из плоского списка диалогов."""
        for i, dialogue in enumerate(dialogues):
            node = DialogueNode(
                index=i,
                dialogue_type=dialogue.get("type", "line"),
                data=dialogue
            )
            self.nodes[i] = node
        
        for i, dialogue in enumerate(dialogues):
            node = self.nodes[i]
            dtype = dialogue.get("type")
            
            if dtype == "line":
                if "next" in dialogue:
                    next_idx = dialogue["next"]
                    if next_idx in self.nodes:
                        node.add_child(self.nodes[next_idx])
                elif "next_scene" not in dialogue:
                    if i + 1 in self.nodes:
                        node.add_child(self.nodes[i + 1])
            
            elif dtype == "jump":
                next_idx = dialogue.get("next")
                if next_idx in self.nodes:
                    node.add_child(self.nodes[next_idx])
            
            elif dtype == "choice":
                for option in dialogue.get("options", []):
                    next_idx = option.get("next")
                    if next_idx in self.nodes:
                        node.add_child(self.nodes[next_idx])
            
            elif dtype == "check_relationship":
                for branch_idx in dialogue.get("branches", {}).values():
                    if branch_idx in self.nodes:
                        node.add_child(self.nodes[branch_idx])
        
        if 0 in self.nodes:
            self.root = self.nodes[0]
    
    def find_all_endings(self):
        """Находит все концовки в дереве (DFS)."""
        endings = []
        
        if not self.root:
            return endings
        
        def dfs(node, path, visited):
            if node.index in visited:
                return
            
            current_path = path + [node.index]
            current_visited = visited | {node.index}
            
            if node.is_ending():
                endings.append({
                    "path": current_path,
                    "ending": node.data.get("next_scene"),
                    "last_text": node.get_text()
                })
                return
            
            if not node.children:
                endings.append({
                    "path": current_path,
                    "ending": "dead_end",
                    "last_text": node.get_text()
                })
                return
            
            for child in node.children:
                dfs(child, current_path, current_visited)
        
        dfs(self.root, [], set())
        return endings
    
    def find_shortest_path(self, target_index):
        """Находит кратчайший путь до узла (BFS)."""
        if not self.root:
            return None
        
        if self.root.index == target_index:
            return [target_index]
        
        queue = [(self.root, [self.root.index])]
        visited = {self.root.index}
        
        while queue:
            current, path = queue.pop(0)
            
            for child in current.children:
                if child.index == target_index:
                    return path + [child.index]
                
                if child.index not in visited:
                    visited.add(child.index)
                    queue.append((child, path + [child.index]))
        
        return None
    
    def get_depth(self):
        """Возвращает максимальную глубину дерева."""
        if not self.root:
            return 0
        
        def dfs_depth(node, visited):
            if node.index in visited or not node.children:
                return 0
            
            visited.add(node.index)
            max_child_depth = 0
            for child in node.children:
                depth = dfs_depth(child, visited)
                max_child_depth = max(max_child_depth, depth)
            
            return 1 + max_child_depth
        
        return dfs_depth(self.root, set())
    
    def get_node_count(self):
        return len(self.nodes)
    
    def get_choice_count(self):
        return sum(1 for n in self.nodes.values() if n.dialogue_type == "choice")
    
    def visualize(self):
        """Текстовая визуализация дерева."""
        if not self.root:
            return "Пустое дерево"
        
        lines = ["=== DialogueTree ==="]
        
        def dfs_print(node, indent=0, visited_set=None):
            if visited_set is None:
                visited_set = set()
            
            if node.index in visited_set:
                prefix = "  " * indent + "└─ "
                text = node.get_text()[:50]
                lines.append(f"{prefix}({node.index}) {text} [цикл]")
                return
            
            visited_set.add(node.index)
            prefix = "  " * indent + ("├─ " if indent > 0 else "")
            text = node.get_text()[:50]
            
            ending_mark = " ★" if node.is_ending() else ""
            type_mark = f"[{node.dialogue_type}]"
            lines.append(f"{prefix}({node.index}) {type_mark} {text}{ending_mark}")
            
            for child in node.children:
                dfs_print(child, indent + 1, visited_set.copy())
        
        dfs_print(self.root)
        return "\n".join(lines)
    
    def get_stats(self):
        """Статистика дерева."""
        endings = self.find_all_endings()
        
        return {
            "total_nodes": self.get_node_count(),
            "choices": self.get_choice_count(),
            "max_depth": self.get_depth(),
            "total_endings": len(endings),
            "unique_endings": len(set(e["ending"] for e in endings)),
            "dead_ends": sum(1 for e in endings if e["ending"] == "dead_end"),
        }