import { create } from "zustand";

const useStore = create((set) => ({
  count: 0,
  inc: () =>
    set((state) => {
      return { count: state.count + 1 };
    }),
  dec: () =>
    set((state) => {
      if (state.count > 0) {
        return { count: state.count - 1 };
      } else {
        return { count: 0 };
      }
    }),
}));

const useNameStore = create((set) => ({
  name: "NaN Ji",
  genderaltered: false,
  setName: (name) =>
    set((state) => {
      return {
        name,
        genderaltered: false
      };
    }),
  boy: () =>
    set((state) => {
      if (state.genderaltered === false) {
        return { name: `${state.name} boy`,genderaltered: true };
      }
      else {
        return { name: `${state.name}` };
      }
    }),
  girl: () =>
    set((state) => {
      if (state.genderaltered === false) {
        return { name: `${state.name} girl`,genderaltered: true };
      }
      else {
        return { name: `${state.name}` };
      }
      
    }),
}));

// const useNameStore = create((set) => ({
//   name: "NaN Ji",
//   setName: (name) =>
//     set((state) => ({
//       name,
//     })),
//   boy: () =>
//     set((state) => ({ name: `${state.name} boy` })), // Use template literal for cleaner string concatenation
//   girl: () =>
//     set((state) => ({ name: `${state.name} girl` })), // Use template literal for cleaner string concatenation
// }));

export { useStore, useNameStore };
