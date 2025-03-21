import { useContext } from 'react'
import { FiltersContext } from './contextSearch'

export function useFilters () {
  const { filters, setFilters } = useContext(FiltersContext)

  
  const filterTraining = (elements) => {
    return elements.filter(elements =>{
        return(
            filters.name === 'All' ? elements.name : (filters.name === elements.name || filters.name === elements.training || filters.name === elements.id.toString())
        )
    })
  }

  return { filters, filterTraining, setFilters }
}

