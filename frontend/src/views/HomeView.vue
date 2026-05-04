<script setup lang="ts">
import { onMounted, computed } from 'vue';
import { useHabitStore } from '@/stores/habits';

import Header from '../components/Header.vue';
import StatsSection from '@/components/StatsSection.vue';
import Footer from '@/components/Footer.vue';
import { TrendingDown, TrendingUp } from 'lucide-vue-next';
import AddHabitForm from '@/components/AddHabitForm.vue';
import HabitCard from '@/components/HabitCard.vue';
import Toast from '@/components/Toast.vue';

import type { Habit } from '@/types/habit';
import { useToastStore } from '@/stores/toast';

const habitStore = useHabitStore();
const toastStore = useToastStore();

const goodHabits = computed(() => habitStore.habits?.filter((h: Habit) => h.type === 'good') ?? []);
const badHabits = computed(() => habitStore.habits?.filter((h: Habit) => h.type === 'bad') ?? []);

onMounted(async () => {
    try {
        await habitStore.fetchHabits();
        await habitStore.fetchAllHabitLogs();
    } catch {
        toastStore.show('Failed to load habits.')
    }
});


</script>

<template>
    <div class="bg-green-100 min-h-screen flex flex-col">
        <Header />
        <Toast />
        <main class="flex-1 p-4">
            <StatsSection />
            <div class="bg-white rounded-xl shadow-md p-6 mb-8 grid grid-cols-1 lg:grid-cols-2 gap-8">
                <section>
                    <div class="flex items-center gap-2 mb-4">
                        <TrendingUp class="w-6 h-6 text-green-600" />
                        <h2 class="text-xl font-semibold text-gray-900">Good Habits</h2>
                        <span class="text-sm text-gray-500">({{ goodHabits?.length }})</span>
                    </div>

                    <div v-if="habitStore.isLoading" class="flex justify-center py-12">
                        <div class="w-8 h-8 border-4 border-green-600 border-t-transparent rounded-full animate-spin"></div>
                    </div>
                    
                    <div v-else>
                        <div class="space-y-3">
                            <AddHabitForm type="good" />
                            <HabitCard
                                v-for="habit in goodHabits"
                                :key="habit.id"
                                :habit="habit"
                            />
                            <p v-if="goodHabits?.length === 0" class="text-center text-gray-500 py-8">No good habits yet. Start building one!</p>
                        </div>
                    </div>
                </section>

                <section>
                    <div class="flex items-center gap-2 mb-4">
                        <TrendingDown class="w-6 h-6 text-red-600" />
                        <h2 class="text-xl font-semibold text-gray-900">Bad Habits</h2>
                        <span class="text-sm text-gray-500">({{ badHabits?.length }})</span>
                    </div>
                    
                    <div v-if="habitStore.isLoading" class="flex justify-center py-12">
                        <div class="w-8 h-8 border-4 border-green-600 border-t-transparent rounded-full animate-spin"></div>
                    </div>

                    <div v-else>
                        <div class="space-y-3">
                            <AddHabitForm type="bad" />
                            <HabitCard
                                v-for="habit in badHabits"
                                :key="habit.id"
                                :habit="habit"
                            />
                            <p v-if="badHabits?.length === 0" class="text-center text-gray-500 py-8">No bad habits tracked. Add one to start breaking it!</p>
                        </div>
                    </div>
                </section>
            </div>
        </main>
        <Footer />
    </div>
</template>