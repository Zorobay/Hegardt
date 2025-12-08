export interface DateInfo {
  date: {
    $date: number
  }
  day: number | null
  month: number | null
  year: number | null
}

export interface Location {
  city: string
  country: string
  notes: string
  region: string
  latitude?: number
  longitude?: number
  fetchStatus?: string
}

export interface LifeEvent {
  date: DateInfo | null
  location: Location | null
  notes: string
}

export interface Marriage {
  date?: DateInfo | null,
  location?: Location| null,
  personId: number
}

export interface Person {
  birth: LifeEvent
  burial: LifeEvent
  children: number[]
  death: LifeEvent
  father: number | null
  fileId: string
  firstName: string
  lastName: string
  marriages: Marriage[]
  middleNames: string[]
  mother: number | null
  notes: string
  occupations: string[]
  references: string[]
  sex: 'MAN' | 'WOMAN' | 'UNKNOWN'
  id: number
}

export interface PersonsData {
  [key: string]: Person
}

