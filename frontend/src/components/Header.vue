<script setup lang="ts">
import { useAuthStore } from '@/stores/auth';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';

import Logo from '@/components/Logo.vue'

const authStore = useAuthStore();
const route = useRoute();
const router = useRouter();

</script>

<template>
<header class="flex justify-between items-center px-6 py-4 bg-white border-b border-b-gray-200">
    <div class="flex justify-between items-center">    
        <Logo class="inline mr-1"/>
        <h1 class="text-xl font-bold inline">Habit Tracker</h1>
    </div>

    <button v-if="route.path==='/'" @click="router.push('/login')" class="text-white bg-green-600 px-6 py-2 rounded-lg font-medium hover:bg-green-700">Get Started</button>
    <button v-else @click="authStore.logout" class="text-white bg-green-600 px-6 py-2 rounded-lg font-medium hover:bg-green-700">Log out</button>
</header>
</template>

<style scoped>
</style>