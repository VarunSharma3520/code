import { useState } from "react";
import reactLogo from "./assets/react.svg";
import { invoke } from "@tauri-apps/api/tauri";
import { writeTextFile, BaseDirectory } from "@tauri-apps/api/fs";
import "./App.css";

function App() {
  const [greetMsg, setGreetMsg] = useState("");
  const [name, setName] = useState("");

  async function greet() {
    setGreetMsg(await invoke("greet", { name }));
  }

  async function saveFile() {
    try {
      await writeTextFile("test.txt", `${greetMsg}`, { dir: BaseDirectory.AppConfig });
      alert("File written successfully!");
    } catch (error) {
      console.error("Error writing file:", error);
      alert("Failed to write file.");
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-800 text-white p-4">
      <h1 className="text-4xl font-bold mb-8">Welcome to Tauri!</h1>

      <div className="flex space-x-4 mb-8">
        <a href="https://vitejs.dev" target="_blank" rel="noopener noreferrer">
          <img src="/vite.svg" className="w-16 h-16" alt="Vite logo" />
        </a>
        <a href="https://tauri.app" target="_blank" rel="noopener noreferrer">
          <img src="/tauri.svg" className="w-16 h-16" alt="Tauri logo" />
        </a>
        <a href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
          <img src={reactLogo} className="w-16 h-16" alt="React logo" />
        </a>
      </div>

      <p className="mb-8 text-lg">
        Click on the Tauri, Vite, and React logos to learn more.
      </p>

      <form
        className="flex flex-col items-center space-y-4"
        onSubmit={(e) => {
          e.preventDefault();
          greet();
        }}
      >
        <input
          id="greet-input"
          className="text-slate-600 px-4 py-2 rounded-lg border-2 border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          onChange={(e) => setName(e.currentTarget.value)}
          placeholder="Enter a name..."
        />
        <button
          type="submit"
          className="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Greet
        </button>
      </form>

      {greetMsg && <p className="mt-8 text-2xl font-semibold">{greetMsg}</p>}

      <button
        onClick={saveFile}
        className="mt-8 px-6 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500"
      >
        Save File
      </button>
    </div>
  );
}

export default App;
