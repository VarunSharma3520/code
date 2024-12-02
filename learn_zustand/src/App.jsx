import { useStore, useNameStore } from "./store";

function App() {
  // const count = useStore((state) => state.count);
  // const inc = useStore((state) => state.inc);
  // const dec = useStore((state) => state.dec);

  const { count, inc, dec } = useStore((state) => ({
    count: state.count,
    inc: state.inc,
    dec: state.dec,
  }));

  const name = useNameStore((state) => state.name);
  const setName = useNameStore((state) => state.setName);
  const boy = useNameStore((state) => state.boy);
  const girl = useNameStore((state) => state.girl);

  return (
    <>
      <div className="card">
        <input
          type="Name"
          placeholder={name}
          onChange={(e) => setName(e.target.value)}
        />

        {[name, count].map((value, index) => {
          console.log(`value: ${value}, index: ${index}`)
          return <p key={index}>{value}</p>;
        })}

        {[
          { label: "Increment", onClick: inc },
          { label: "Decrement", onClick: dec },
          { label: 'Add "boy"', onClick: boy },
          { label: 'Add "girl"', onClick: girl },
        ].map((action, index) => (
          <>
            <button key={index} onClick={action.onClick}>
              {action.label}
            </button>
            <br />
          </>
        ))}
      </div>
    </>
  );
}

export default App;
