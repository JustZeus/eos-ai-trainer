import "./dashboard.css"
import { CustomSelect } from "./components/selectComponent/customSelect"
import {OptionSelectProvider } from "./components/selectComponent/selectContext"
import { HeadApp } from "./components/head/head"
import {FiltersProvider} from "./components/head/contextSearch"
import { TrainingApp } from "./components/cardTraining"
import {CurrentTraining} from "./components/cardTraining"

function NoRunning(){
    return(
        <div className="noRunning">
            <h2>No training is currently running.</h2>
            <span>You can start a new workout or resume one you've already created.</span>
        </div>
    )
}



export function DashboardApp(){
    // Change the value to "false" to see the interface when there are no active trainings and "true" for when running.
    let currentlyTraining = true;
    return(
        <div className="dashboardSection">
            <FiltersProvider>
            <OptionSelectProvider>
                <HeadApp/>            
            <main>
                <article className="newNowTraining">
                    <div className="NewTraining">
                        <div>
                            <h2>Start a new workout</h2>
                            <div className="submitNetTraining">
                                    <CustomSelect/>
                            </div>
                            <div className='note'>
                                    <div>!</div><p>To start a new training you shouldn't have any active training</p>
                            </div>
                        </div>
                            <button className="submit"><p>Start</p></button>
                    </div>
                    <div className="line"></div>
                    {
                        currentlyTraining ?<CurrentTraining/> : <NoRunning />

                    }                   
                </article>
                <TrainingApp/> 
            </main>
            </OptionSelectProvider>
            </FiltersProvider>         
        </div>
    )
}