import { defineStore } from "pinia";
import { ref } from "vue";
import { http } from "@/api/axios";
import type { Habit } from "@/types/habit";

export const useHabitStore = defineStore("habits", () => {
    const habits = ref<Habit[] | null>(null);

    async function fetchHabits() {
        const response = await http.get('/habits/');
        habits.value = response.data;
    }

    async function createHabit(title: string, desc: string, start_date: string, type: string) {
        await http.post('/habits/', { title, desc, start_date, type });
        fetchHabits();
    }

    async function updateHabit(id: number, title: string, desc: string, start_date: string, type: string) {
        await http.put(`/habits/${id}/`, { title, desc, start_date, type });
        fetchHabits();
    }

    async function deleteHabit(id: number) {
        await http.delete(`/habits/${id}/`);
        fetchHabits();
    }

    async function fetchHabitLogs(id: number) {
        const response = await http.get(`/habits/${id}/log/`);
        for (const habit of habits.value ?? []) {
            if (habit.id === id) {
                habit.logs = response.data;
            }
        }
    }

    async function logHabit(id: number) {
        const date: Date = new Date();
        const dateToSend: string = date.toLocaleDateString('en-CA');
        await http.post(`/habits/${id}/log/`, { "log_date": dateToSend });
        fetchHabitLogs(id);
    }

    async function deleteHabitLog(habitLogId: number, habitId: number) {
        await http.delete(`/habits/${habitId}/log/${habitLogId}/`);
        fetchHabitLogs(habitId);
    }

    return { habits, fetchHabits, createHabit, updateHabit, deleteHabit, fetchHabitLogs, logHabit, deleteHabitLog }
});