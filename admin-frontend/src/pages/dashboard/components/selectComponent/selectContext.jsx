import { createContext, useState } from 'react'

export const OptionSelectContext = createContext()

export function OptionSelectProvider ({ children }) {
  const [optionSelect, setOptionSelect] = useState("Select your new training")

  return (
    <OptionSelectContext.Provider value={{
        optionSelect, 
        setOptionSelect
    }}
    >
      {children}
    </OptionSelectContext.Provider>
  )
}