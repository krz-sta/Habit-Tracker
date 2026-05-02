<script setup lang="ts">
import Header from '@/components/Header.vue';
import { useRouter } from 'vue-router';
import { TrendingUp, TrendingDown, Target, Calendar, BarChart3, CheckCircle2, TrendingUpIcon, TrendingUpDown, LucideTrendingUp, TrendingDownIcon } from 'lucide-vue-next';

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
                <button @click="router.push('/home')" class="px-8 py-4 rounded-lg bg-green-600 hover:bg-green-700 text-white font-semibold text-lg shadow-lg hover:shadow-lx transition-all">Start Tracking</button>
            </section>

            <section class="max-w-7xl mx-auto px-4 py-16">
                <div class="grid grid-cols-1 md:grid-cols-2 lg-grid-cols-3 gap-8">
                    <div class="bg-white rounded-xl p-6 shadow-md">
                        <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
                            <TrendingUp class="w-6 h-6 text-green-600" />
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Good Habits</h3>
                        <p class="text-gray-600">
                            Build positive routines like exercise, reading or meditation.
                            Track your progress and celebrate wins.
                        </p>
                    </div>

                    <div class="bg-white rounded-xl p-6 shadow-md">
                        <div class="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center mb-4">
                            <TrendingDownIcon class="w-6 h-6 text-red-600" />
                        </div>
                        <h3 class="text-xl font-semibold text-gray-900 mb-2">Break Bad Habits</h3>
                        <p class="text-gray-600">
                            Identify and eliminate negative patterns. Stay accountable
                            with daily tracking and streak monitoring.
                        </p>
                    </div>

                            <div class="bg-white rounded-xl p-6 shadow-md">
                    <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                        <Calendar class="w-6 h-6 text-blue-600" />
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-2">Daily Check-ins</h3>
                    <p class="text-gray-600">
                        Simple one-tap check-ins make tracking effortless.
                        Build consistency with daily reminders.
                    </p>
                    </div>

                    <div class="bg-white rounded-xl p-6 shadow-md">
                    <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                        <BarChart3 class="w-6 h-6 text-purple-600" />
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-2">Streak Tracking</h3>
                    <p class="text-gray-600">
                        Watch your streaks grow as you stay consistent.
                        Visual progress keeps you motivated.
                    </p>
                    </div>

                    <div class="bg-white rounded-xl p-6 shadow-md">
                    <div class="w-12 h-12 bg-yellow-100 rounded-lg flex items-center justify-center mb-4">
                        <CheckCircle2 class="w-6 h-6 text-yellow-600" />
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-2">Personal Account</h3>
                    <p class="text-gray-600">
                        Your habits are private and secure. Access your data
                        from any device, anytime.
                    </p>
                    </div>

                    <div class="bg-white rounded-xl p-6 shadow-md">
                    <div class="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mb-4">
                        <Target class="w-6 h-6 text-indigo-600" />
                    </div>
                    <h3 class="text-xl font-semibold text-gray-900 mb-2">Stay Focused</h3>
                    <p class="text-gray-600">
                        Clean, distraction-free interface helps you focus on
                        what matters: building better habits.
                    </p>
                    </div>
                </div>
            </section>

            <section class="bg-green-600 text-white py-20">
                <div class="max-w-4xl mx-auto px-4 text-center">
                    <h2 class="text-4xl font-bold mb-6">Ready to Transform Your Life?</h2>
                    <p class="text-xl mb-8 text-green-50">Be the first to build better habits every day.</p>
                    <button @click="router.push('/home')" class="px-8 py-4 rounded-lg bg-white hover:bg-gray-100 text-green-600 font-semibold text-lg shadow-lg transition-all">Create Your Account</button>
                </div>
            </section>
        </main>
    </div>

</template>

<style scoped></style>