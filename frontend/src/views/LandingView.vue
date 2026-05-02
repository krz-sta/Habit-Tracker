<script setup lang="ts">
import Header from '@/components/Header.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

</script>

<template>
    <div class="bg-green-50 min-h-screen">
        <Header />
        <main>
            <section class="max-w-7xl mx-auto px-4 py-20 text-center">
                <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6">Build Better Habits, <br />
                    One Day at a Time
                </h1>
                <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
                    Track your daily habits, build powerful streaks, and transform your life through consistent small actions.
                </p>
                <button @click="router.push('/auth')" class="px-8 py-4 rounded-lg bg-green-600 hover:bg-green-700 text-white font-semibold text-lg shadow-lg hover:shadow-lx transition-all">Start Tracking</button>
            </section>
        </main>
    </div>

</template>

<style scoped></style>