This cheatsheet covers the fundamental aspects of React-Redux[official React-Redux documentation](https://react-redux.js.org/).

### Step 1: Set Up Your React Project

If you haven't already created a React project, you can do so using Create React App:

```bash
npx create-react-app my-todo-app
cd my-todo-app
```

### Step 2: Install Redux and React-Redux

Install Redux and React-Redux libraries:

```bash
npm install redux react-redux
```

### Step 3: Create Redux Store

Create a `store` directory in your `src` folder and add a `store.js` file:

```javascript
// src/store/store.js
import { createStore } from 'redux';
import rootReducer from './reducers';

const store = createStore(rootReducer);

export default store;
```

### Step 4: Create a Root Reducer

Create a `reducers` directory in your `src/store` folder and add an `index.js` file:

```javascript
// src/store/reducers/index.js
import { combineReducers } from 'redux';
import todoReducer from './todoReducer';

const rootReducer = combineReducers({
  todos: todoReducer,
});

export default rootReducer;
```

### Step 5: Create a Todo Reducer

Create a `todoReducer.js` file in your `src/store/reducers` directory:

```javascript
// src/store/reducers/todoReducer.js
const initialState = {
  todos: [],
};

const todoReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'ADD_TODO':
      return { ...state, todos: [...state.todos, action.payload] };
    case 'REMOVE_TODO':
      return { ...state, todos: state.todos.filter((_, index) => index !== action.payload) };
    default:
      return state;
  }
};

export default todoReducer;
```

### Step 6: Provide the Redux Store to Your App

In your `src/index.js` file, wrap your `App` component with the `Provider` component from `react-redux` and pass the store to it:

```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './store/store';
import App from './App';

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

### Step 7: Connect Your Components to Redux

Create a `TodoList` component and a `TodoForm` component in your `src` directory.

#### TodoList Component

```javascript
// src/TodoList.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

const TodoList = () => {
  const todos = useSelector((state) => state.todos.todos);
  const dispatch = useDispatch();

  const removeTodo = (index) => {
    dispatch({ type: 'REMOVE_TODO', payload: index });
  };

  return (
    <div>
      <h2>Todo List</h2>
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo} <button onClick={() => removeTodo(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
```

#### TodoForm Component

```javascript
// src/TodoForm.js
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';

const TodoForm = () => {
  const [input, setInput] = useState('');
  const dispatch = useDispatch();

  const addTodo = (e) => {
    e.preventDefault();
    if (input.trim()) {
      dispatch({ type: 'ADD_TODO', payload: input });
      setInput('');
    }
  };

  return (
    <form onSubmit={addTodo}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Add a new todo"
      />
      <button type="submit">Add Todo</button>
    </form>
  );
};

export default TodoForm;
```

### Step 8: Use the Todo Components in Your App

Modify your `App.js` file to include the `TodoList` and `TodoForm` components:

```javascript
// src/App.js
import React from 'react';
import TodoList from './TodoList';
import TodoForm from './TodoForm';

const App = () => {
  return (
    <div className="App">
      <h1>Todo App</h1>
      <TodoForm />
      <TodoList />
    </div>
  );
};

export default App;
```

### Summary

You've now set up a basic Todo application using React and Redux. Here’s a quick summary of what we did:

1. **Created a React project**.
2. **Installed Redux and React-Redux**.
3. **Created a Redux store**.
4. **Created a root reducer**.
5. **Created a todo reducer**.
6. **Provided the Redux store to the app**.
7. **Connected React components to Redux** using `useSelector` and `useDispatch` hooks.

### Example File Structure

```
my-todo-app
├── node_modules
├── public
├── src
│   ├── store
│   │   ├── reducers
│   │   │   ├── todoReducer.js
│   │   │   └── index.js
│   │   └── store.js
│   ├── App.js
│   ├── TodoForm.js
│   ├── TodoList.js
│   ├── index.css
│   ├── index.js
│   └── ...
├── package.json
├── README.md
└── ...
```

With this setup, you now have a working Redux-powered Todo application in React. You can extend this setup by adding more actions, reducers, and components as needed.
