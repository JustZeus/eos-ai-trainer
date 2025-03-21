import "./font/stylesheet.css"
import { useContext } from "react"
import {Login} from "./pages/login/login"
import {DashboardApp} from "./pages/dashboard/dashboard"
import { LoginProvider, LoginContext} from "./pages/login/loginContext"


function Page(){
  const { login, setLogin} = useContext(LoginContext)

  return(
    <>
      {
        (login.user == "admin" && login.password == "Tanji2025") ?
        <DashboardApp/>:
        <Login /> 
      }
    </>
  )
}
function App() {

  return (
    <>
      <LoginProvider>
        <Page />
      </ LoginProvider>
     
    </>
  )
}

export default App
