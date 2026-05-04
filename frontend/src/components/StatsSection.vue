<script setup lang="ts">
import StatCard from './StatCard.vue';
import { Target, TrendingUp, Flame, Calendar } from 'lucide-vue-next';
import { useHabitStore } from '@/stores/habits';
import { computed } from 'vue';
import type { Habit } from '@/types/habit';
import type { HabitLog } from '@/types/habitLog';

const habitStore = useHabitStore();

const countCompletedToday = computed(() => {
    const today = new Date().toLocaleDateString('en-CA');
    return habitStore.habits?.filter((habit: Habit) => habit.logs?.some((log) => log.log_date === today)).length ?? 0;
});

const countCompletedThisWeek = computed(() => {
    const startOfWeek = new Date()
    startOfWeek.setHours(0, 0, 0, 0)
    const day = startOfWeek.getDay() || 7
    startOfWeek.setDate(startOfWeek.getDate() - day + 1)

    const start = startOfWeek.toLocaleDateString('en-CA')
    return habitStore.habits?.flatMap((h: Habit) => h.logs ?? []).filter((log: HabitLog) => log.log_date >= start).length ?? 0
})

const bestAllTimeStreak = computed(() => {
    if (!habitStore.habits) return 0
    return Math.max(0, ...habitStore.habits
        .filter((h: Habit) => h.type === 'good')
        .map((h: Habit) => {
            if (!h.logs || h.logs.length === 0) return 0
            const sorted = [...h.logs]
                .map(l => l.log_date)
                .sort((a, b) => a.localeCompare(b))
            
            let best = 1
            let current = 1

            for (let i = 1; i < sorted.length; i++) {
                const prevStr = sorted[i - 1]
                const currStr = sorted[i]
                if (!prevStr || !currStr) continue

                const prev = new Date(prevStr)
                const curr = new Date(currStr)
                prev.setDate(prev.getDate() + 1)

                if (prev.toLocaleDateString('en-CA') === curr.toLocaleDateString('en-CA')) {
                    current++
                    best = Math.max(best, current)
                } else {
                    current = 1
                }
            }
            return best
        })
    )
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
        
        <StatCard label="Best Streak" :value="bestAllTimeStreak" bg-color="bg-orange-50">
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