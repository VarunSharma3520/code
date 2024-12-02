import { useStore, useNameStore } from "./store";

function App() {
  // const count = useStore((state) => state.count);
  // const inc = useStore((state) => state.inc);
  // const dec = useStore((state) => state.dec);
  //                 or
  const { count, inc, dec } = useStore((state) => (state));

  const name = useNameStore((state) => state.name);
  const setName = useNameStore((state) => state.setName);
  const boy = useNameStore((state) => state.boy);
  const girl = useNameStore((state) => state.girl);

  return (
      <div className="card">
        <input
          type="Name"
          placeholder={name}
        onChange={(e) => {
            e.preventDefault();
            setName(e.target.value);
          }}
        />

        <p>Name: {name}</p>
        <p>Count: {count}</p>

        {[
          { label: "Increment", onClick: inc },
          { label: "Decrement", onClick: dec },
          { label: 'Add "boy"', onClick: boy },
          { label: 'Add "girl"', onClick: girl },
        ].map((value, index) => (
          <>
            <button key={index} onClick={value.onClick}>
              {value.label}
            </button>
          </>
        ))}
      </div>
  );
}

export default App;
