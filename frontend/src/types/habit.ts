import type { HabitLog } from "./habitLog"

export interface Habit {
    id: number,
    owner: number,
    title: string,
    desc: string,
    startDate: string,
    type: string,
    logs: HabitLog[]
}