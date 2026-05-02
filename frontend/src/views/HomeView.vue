<script setup lang="ts">
import { onMounted } from 'vue';
import { useHabitStore } from '@/stores/habits';
import { useAuthStore } from '@/stores/auth';

import Header from '../components/Header.vue';
import StatsSection from '@/components/StatsSection.vue';
import Footer from '@/components/Footer.vue';
import { TrendingDown, TrendingUp } from 'lucide-vue-next';

const habitStore = useHabitStore();
const authStore = useAuthStore();

onMounted(async () => {
    await habitStore.fetchHabits();
});

</script>

<template>
    <div class="bg-green-100 min-h-screen flex flex-col">
        <Header />
        <main class="flex-1 p-4">
            <StatsSection />
            <section class="bg-white rounded-xl shadow-md p-6 mb-8">
                <section>
                    <div class="flex items-center gap-2 mb-4">
                        <TrendingUp class="w-6 h-6 text-green-600" />
                        <h2 class="text-xl font-semibold text-gray-900">Good Habits</h2>
                        <span class="text-sm text-gray-500">(0)</span>
                    </div>
                </section>

                <section>
                    <div class="flex items-center gap-2 mb-4">
                        <TrendingDown class="w-6 h-6 text-red-600" />
                        <h2 class="text-xl font-semibold text-gray-900">Bad Habits</h2>
                        <span class="text-sm text-gray-500">(0)</span>
                    </div>
                </section>
            </section>
        </main>
        <Footer />
    </div>
</template>