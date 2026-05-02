<script setup lang="ts">
import { useHabitStore } from '@/stores/habits';
import type { Habit } from '@/types/habit';
import { Check, TrendingUp, Trash2, RefreshCcw } from 'lucide-vue-next';

defineProps<{
    habit: Habit
}>()

const habitStore = useHabitStore();

const today: string = '01-01-2001';
const isCompletedToday: boolean = false;
const streak: number = 11;

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
                    <span>X day streak</span>
                </div>
                <div v-if="habit.type === 'good'" class="text-sm text-gray-600">
                    {{ habit.logs?.length ?? 0 }} total
                </div>
            </div>
        </div>

        <div class="flex gap-2">
            <button
                :class="`p-2 rounded-md transition-colors ${
                    isCompletedToday
                        ? habit.type === 'good'
                            ? 'bg-green-500 text-white'
                            : 'bg-red-500 text-white'
                        : 'bg-white border border-gray-300 hover:bg-gray-50'
                }`"
            >
                <Check v-if="habit.type === 'good'" class="w-5 h-5"/>
                <RefreshCcw v-else class="w-5 h-5" />
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