<script setup lang="ts">
import { onMounted } from 'vue';
import { useHabitStore } from '@/stores/habits';
import { useAuthStore } from '@/stores/auth';

import CreateHabitForm from './CreateHabitForm.vue';
import Header from '../components/Header.vue';

const habitStore = useHabitStore();
const authStore = useAuthStore();

onMounted(async () => {
    await habitStore.fetchHabits();
});

</script>

<template>
    <div class="bg-green-100">
        <Header />
        <ul>
            <li v-for="habit in habitStore.habits">{{ habit.title }}, {{ habit.start_date }}</li>
        </ul>
        <CreateHabitForm />
    </div>
</template>