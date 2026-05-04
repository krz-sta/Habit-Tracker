<script setup lang="ts">
import { useHabitStore } from '@/stores/habits';
import type { Habit } from '@/types/habit';
import { Check, TrendingUp, Trash2, RefreshCcw } from 'lucide-vue-next';
import { computed } from 'vue';

const { habit } = defineProps<{
    habit: Habit
}>()

const badHabitStreak = computed(() => {
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    const startDate = new Date(habit.start_date)
    startDate.setHours(0, 0, 0, 0)
    const diffMs = today.getTime() - startDate.getTime()
    return Math.floor(diffMs / (1000 * 60 * 60 * 24))
})

function calculateStreak () {
    if (!habit.logs || habit.logs.length === 0) return 0;

    const sorted = [...habit.logs]
        .map(l => l.log_date)
        .sort((a, b) => b.localeCompare(a));

    let streak = 0;
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    for (const logDate of sorted) {
        const expected = new Date(today);
        expected.setDate(today.getDate() - streak);
        const expectedStr = expected.toLocaleDateString('en-CA');

        if (logDate === expectedStr) {
            streak++;
        } else {
            break;
        }
    }
    return streak;
} 

const habitStore = useHabitStore();

const today: string = '01-01-2001';

const isCompletedToday = computed(() => {
    const todayStr = new Date().toLocaleDateString('en-CA');
    return habit.logs?.some(log => log.log_date === todayStr) ?? false;
});

async function handleResetBadHabitStreak() {
    const date: Date = new Date();
    const dateToSend: string = date.toLocaleDateString('en-CA');
    await habitStore.updateHabit(habit.id, habit.title, habit.desc, dateToSend, habit.type);
}

async function handleToggleHabitLog() {
    console.log("xyz")
    console.log(isCompletedToday.value)
    if (isCompletedToday.value) {
        const today = new Date().toLocaleDateString('en-CA');
        const todaysHabitLog = habit.logs.find((log) => log.log_date === today);
        if (todaysHabitLog?.id) {
            habitStore.deleteHabitLog(todaysHabitLog.id, habit.id);
        }
    } else {
        console.log("logging")
        habitStore.logHabit(habit.id);
    }
}

</script>

<template>
<div :class="`p-4 rounded-lg border-2 ${
    habit.type === 'good'
        ? 'bg-green-50 border-green-200'
        : 'bg-red-50 border-red-200'
    }`">
    <div class="flex items-start justify-between gap-3">
        <div class="flex1 min-w-0">
            <h3 class="font-medium truncate">{{ habit.title }}</h3>
            <p v-if="habit.desc" class="text-sm text-gray-600 mt-1">{{ habit.desc }}</p>
            <div class="flex items-center gap-4 mt-2">
                <div class="flex items-center gap-1 text-sm">
                    <TrendingUp class="w-4 h-4" />
                    <span v-if="habit.type === 'good'" >{{ calculateStreak() }} day streak</span>
                    <span v-if="habit.type === 'bad'">{{ badHabitStreak }} day streak</span>
                </div>
                <div v-if="habit.type === 'good'" class="text-sm text-gray-600">
                    {{ habit.logs?.length ?? 0 }} total
                </div>
            </div>
        </div>

        <div class="flex gap-2">
            <button v-if="habit.type === 'good'"
                :class="`p-2 rounded-md transition-colors ${
                    isCompletedToday
                        ? habit.type === 'good'
                            ? 'bg-green-500 text-white'
                            : 'bg-red-500 text-white'
                        : 'bg-white border border-gray-300 hover:bg-gray-50'
                }`"
                @click="handleToggleHabitLog()"
            >
                <Check class="w-5 h-5" />
            </button> 
            <button v-else @click="handleResetBadHabitStreak()" class="p-2 rounded-md bg-white border border-gray-300 hover:bg-gray-50 text-gray-700">
                <RefreshCcw class="w-5 h-5" />
            </button>
            <button
                @click="habitStore.deleteHabit(habit.id)"
                class="p-2 rounded-md bg-white border border-gray-300 hover:bg-gray-50 text-gray-700"
            >
                <Trash2 class="w-5 h-5" />
            </button>
        </div>
    </div>
</div>
</template>

<style scoped></style>