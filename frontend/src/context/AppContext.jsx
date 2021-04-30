import { createContext, useContext, useState } from "react";

const AppContext = createContext();

export function AppWrapper({ children, appLink }) {
  const [darkMode, setDarkMode] = useState();

  let sharedState = {
    setDarkMode,
    darkMode,
  };

  return (
    <AppContext.Provider value={sharedState}>{children}</AppContext.Provider>
  );
}

export const useAppContext = () => {
  return useContext(AppContext);
};
