import { useContext  } from 'react';
import {OptionSelectContext} from "./selectContext"
import './CustomSelect.css'; 

const suppliers = [
    {id:1, label:"Training 1. Assembly D21"},
    {id:2, label:"Training 2. Assembly M10"},
    {id:3, label:"Training 3. Assembly A96"},
    {id:4, label:"Training 4. Assembly N25"},
]

 
export function CustomSelect(){
  const {optionSelect, setOptionSelect} = useContext(OptionSelectContext)

  function handleOption(op){
    setOptionSelect(op)
  }

  return(
    
      <div className="select-menu">
        <label>
          <input type="checkbox" className="checkBoxSelectMap"/>
          <div className="select-btn">
              <span className="sBtn-text">{optionSelect}</span>
          </div>

          <ul className="options">
              {suppliers.map(optionMap => (
                  <li className="option" key={optionMap.id} onClick={() => handleOption(optionMap.label)}>
                      <span className="option-text">{optionMap.label}</span>
                  </li>
              ))}
          </ul>
        </label>
      </div>
  )
}