<script setup lang="ts">
import { onMounted } from 'vue';
import { useHabitStore } from '@/stores/habits';
import { useAuthStore } from '@/stores/auth';

import CreateHabitForm from './CreateHabitForm.vue';

const habitStore = useHabitStore();
const authStore = useAuthStore();

onMounted(async () => {
    await habitStore.fetchHabits();
});

</script>

<template>
    <h1>Habit Tracker</h1>
    <ul>
        <li v-for="habit in habitStore.habits">{{ habit.title }}, {{ habit.start_date }}</li>
    </ul>
    <button @click="authStore.logout">Logout</button>
    <CreateHabitForm />
</template>