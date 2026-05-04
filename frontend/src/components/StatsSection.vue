<script setup lang="ts">
import StatCard from './StatCard.vue';
import { Target, TrendingUp, Flame, Calendar } from 'lucide-vue-next';
import { useHabitStore } from '@/stores/habits';
import { computed } from 'vue';

const habitStore = useHabitStore();

const countCompletedToday = computed(() => {
    const today = new Date().toLocaleDateString('en-CA');
    return habitStore.habits?.filter((habit) => habit.logs.some((log) => log.log_date === today)).length ?? 0;
});

const countCompletedThisWeek = computed(() => {
    const startOfWeek = new Date()
    startOfWeek.setHours(0, 0, 0, 0)
    const day = startOfWeek.getDay() || 7
    startOfWeek.setDate(startOfWeek.getDate() - day + 1)

    const start = startOfWeek.toLocaleDateString('en-CA')
    return habitStore.habits?.flatMap(h => h.logs ?? []).filter(log => log.log_date >= start).length ?? 0
})


</script>

<template>
<section class="bg-white rounded-xl shadow-md p-6 mb-8">
    <h2 class="text-xl font-semibold text-gray-900 mb-6">Your Stats</h2>

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        <StatCard label="Total Habits" :value="habitStore.habits?.length ?? 0" bg-color="bg-blue-50">
            <template #icon>
                <Target class="w-6 h-6 text-blue-600"/>
            </template>
        </StatCard>
        
        <StatCard label="Completed Today" :value="countCompletedToday" bg-color="bg-green-50">
            <template #icon>
                <TrendingUp class="w-6 h-6 text-green-600"/>
            </template>
        </StatCard>
        
        <StatCard label="Best Streak" value="0" bg-color="bg-orange-50">
            <template #icon>
                <Flame class="w-6 h-6 text-orange-600"/>
            </template>
        </StatCard>

        <StatCard label="Completions This Week" :value="countCompletedThisWeek" bg-color="bg-indigo-50">
            <template #icon>
                <Calendar class="w-6 h-6 text-indigo-600"/>
            </template>
        </StatCard>
    </div>
</section>
</template>

<style scoped></style>