import { useContext } from "react"
import {LoginContext} from "../../../login/loginContext"
import { useFilters } from "./useFiltersSeach"


export function HeadApp(){
    const { filters, setFilters } = useFilters()
    const { login, setLogin} = useContext(LoginContext)

    const search = (event) =>{
        let newQuery = event.target.value

        if(!newQuery){
            newQuery = "All"
        }
        setFilters(prevState => ({
            ...prevState,
            name: newQuery.charAt(0).toUpperCase() + newQuery.slice(1),
        }))
        // console.log(filters)
    }


    const logOutUser = () => {
        setLogin({ user: "", password: ""})
    };

    return(
        <header>
            <div className="headContainer">
                <div className="brand">
                    <p>EOS</p>
                    <p>Enhanced Orienting Space</p>
                </div>
                <div className="right">
                    <div className="search">
                        <input type="search" placeholder='Seek training...' onChange={search} />
                    </div>
                    <button  className="logout" onClick={logOutUser}>Log out</button>
                </div>
        
            </div>
          
        </header>
    )
}