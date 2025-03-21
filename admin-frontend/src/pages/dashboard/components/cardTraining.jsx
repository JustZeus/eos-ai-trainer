import {trainingList}  from "./example"
import { useFilters } from "./head/useFiltersSeach"
import "./cardTraining.css"


function BarPercent({percent}){
    let progress = (percent*176)/100 + "px"
    return(
        <div className="percentContainer">
            <p>Progress</p>
            <div className="container">
                <div className="outer">
                    <div className="inner" style={{width: progress}}></div>
                </div>
                <div className="percent">{percent}%</div>
            </div>
        </div>
    )
}


export function CurrentTraining(){
    return(
        <div className="nowTraining">
            <div className="left">

                <h2>Currently active training</h2>
                <p>
                    Is currently running in training number
                    <span className="numberTraining">{trainingList[0].id}</span> 
                </p>
                <p style={{color: trainingList[0].active && "#11c26f", fontWeight:trainingList[0].active && "500"}}>{trainingList[0].active ? "Active training" : "There is no active training"}</p>

                <button className="btn stop">Stop</button>
            </div>
              
            <div>
                <h4>{trainingList[0].training}. {trainingList[0].name}</h4>
                <BarPercent percent={trainingList[0].progress}/>
            </div>
                
        </div>
    )
}


function CardTraining({trainingList}){
    return(
        <div className='card-list' >
            {trainingList.map(training => (
                <div key={training.id} className="card-item">
                    <div className="c"></div>
                    <div className="numberTraining">
                        <div>{training.id}</div>
                    </div> 
                    <div className="card-body">
                        <h4>{training.training} <br /> {training.name}</h4>
                        <p style={{color: training.active && "#11c26f", fontWeight:training.active && "500"}}>{training.active ? "Active training" : "There is no active training"}</p>
                        <BarPercent percent={training.progress}/>
                        <div className="buttons">
                            <button className="btn start">Start</button>
                            <button className="btn stop">Stop</button>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    )
}

export function TrainingApp(){
    const { filterTraining} = useFilters()
  
    const filtered = filterTraining(trainingList)
    return(
        <article className="sectionTraining">
            <div className="head">
                <h2>Created workouts</h2>
                <p><span>Total created:</span> {trainingList.length}</p>
            </div>
            <div className='slider-wrapper'>
                <CardTraining trainingList={filtered}/>
            </div>
        </article>
   
    )
}
