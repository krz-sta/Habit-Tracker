import { defineStore } from "pinia";
import { ref } from "vue";
import { http } from "@/api/axios";
import type { Habit } from "@/types/habit";

export const useHabitStore = defineStore("habits", () => {
    const habits = ref<Habit[] | null>([]);
    const isLoading = ref<boolean>(false);

    async function fetchHabits() {
        isLoading.value = true;
        try {
            const response = await http.get('/habits/');
            habits.value = response.data;
        } finally {
            isLoading.value = false;
        }
    }

    async function createHabit(title: string, desc: string, type: string) {
        const date: Date = new Date();
        const dateToSend: string = date.toLocaleDateString('en-CA');
        await http.post('/habits/', { title, desc, "start_date": dateToSend, type });
        await fetchHabits();
        await fetchAllHabitLogs();
    }

    async function updateHabit(id: number, title: string, desc: string, start_date: string, type: string) {
        await http.put(`/habits/${id}/`, { title, desc, start_date, type });
        await fetchHabits();
        await fetchAllHabitLogs();
    }

    async function deleteHabit(id: number) {
        await http.delete(`/habits/${id}/`);
        await fetchHabits();
        await fetchAllHabitLogs();
    }

    async function fetchAllHabitLogs() {
        isLoading.value = true;
        try {
            const response = await http.get(`/habits/log/`);
            
            for (const habit of habits.value ?? []) {
                habit.logs = [];
            }
    
            for (const habitLog of response.data) {
                for (const habit of habits.value ?? []) {
                    if (habitLog.habit == habit.id) {
                        habit.logs.push(habitLog);
                    }
                }
            }
        } finally {
            isLoading.value = false;
        }
    }

    async function logHabit(id: number) {
        const date: Date = new Date();
        const dateToSend: string = date.toLocaleDateString('en-CA');
        await http.post(`/habits/${id}/log/`, { "log_date": dateToSend });
        await fetchAllHabitLogs();
    }

    async function deleteHabitLog(habitLogId: number, habitId: number) {
        await http.delete(`/habits/${habitId}/log/${habitLogId}/`);
        await fetchAllHabitLogs();
    }

    return { habits, fetchHabits, createHabit, updateHabit, deleteHabit, fetchAllHabitLogs, logHabit, deleteHabitLog, isLoading }
});