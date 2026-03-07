import time

class TODO:
    todos = []
    
    def add_todo(self, desc):

        self.todos.append({'id': int(time.time()),
                            "desc": desc,
                            "is_completed": False,
                        })
    
    def remove_todo(self, id):
        for todo in self.todos:
            if id == todo['id']:
                self.todos.remove(todo)
                return 
        return "ID not found"
    
    def display_todos(self):
        if len(self.todos) == 0:
            return "No Todos"
        for todo in self.todos:
            print(f'{todo['desc']} {todo['id']} {'Completed' if todo['is_completed'] else "incomplete"}')
    
    def update_todo(self, id, new_desc):
        for todo in self.todos:
            if id == todo['id']:
                todo['desc'] = new_desc
                return
        return 'Task not Found'
    
    def toggle_mark_as_completed(self, id):
        for todo in self.todos:
            if id == todo['id']:
                todo['is_completed'] = not todo['is_completed']
                return
    
    def completed_todos(self):
        flag = False
        for todo in self.todos:
            if todo['is_completed']:
                flag = True
                print(todo['desc'])
            
        if not flag:
            print("No completed task")
        
    def incompleted_todos(self):
        flag = False
        for todo in self.todos:
            if not todo['is_completed']:
                flag = True
                print(todo['desc'])

        if not flag:
            print("No incomplete task")
        
