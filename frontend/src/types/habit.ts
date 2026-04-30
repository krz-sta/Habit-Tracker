import type { HabitLog } from "./habitLog"

export interface Habit {
    id: number,
    owner: number,
    title: string,
    desc: string,
    start_date: string,
    type: string,
    logs: HabitLog[]
}