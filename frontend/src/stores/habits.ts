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
        await http.put(`/habits/${id}`, { title, desc, start_date, type });
        fetchHabits();
    }

    async function deleteHabit(id: number) {
        await http.delete(`/habits/${id}/`)
        fetchHabits();
    }

    return { habits, fetchHabits, createHabit, updateHabit, deleteHabit }
});