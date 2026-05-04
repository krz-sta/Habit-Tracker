<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useToastStore } from '@/stores/toast';
import Toast from '@/components/Toast.vue';

const router = useRouter();
const authStore = useAuthStore();
const toastStore = useToastStore();

const username = ref('');
const password = ref('');
const isLogin = ref<boolean>(true);

async function handleLogin() {
    try {
        await authStore.login(username.value, password.value);
        router.push('/home');
    } catch (e: any) {
        toastStore.show(e.response?.data?.detail ?? 'Login failed')
    }
}

async function handleRegister() {
    if (username.value.trim().length < 4) {
        toastStore.show('Username must be at least 4 characters long.');
        return;
    }
    if (password.value.trim().length < 8) {
        toastStore.show('Password must be at least 8 characters long.');
        return;
    }
    try {
        await authStore.register(username.value, password.value)
        username.value = '';
        password.value = '';
        isLogin.value = true;
        router.push('/home');
    } catch (e: any) {
        if (e.response?.data?.username) {
            toastStore.show(e.response?.data?.username?.[0] ?? 'Register failed')
            return
        }
        toastStore.show(e.response?.data?.detail[0] ?? 'Register failed')
    }
}

async function handleSubmit() {
    if (isLogin.value) {
        await handleLogin();
    } else {
        await handleRegister();
    }
}

</script>

<template>
    <Toast />
    <div class="min-h-screen bg-green-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-xl shadow-lg p-8 w-full max-w-md relative">
            <button @click="router.push('/')" class="absolute top-6 left-6">←</button>
            <div class="text-center mb-8">
                <h1 class="text-3xl font-bold mb-2 m-y-2">Habit Tracker</h1>
                <p class="text-gray-600 ">{{ isLogin ? 'Welcome back!' : 'Create an account' }}</p>
            </div>
            <form @submit.prevent="handleSubmit()">
                <div class="text-sm font-medium text-gray-700 mb-5">
                    <label class="block text-sm font-medium text-gray-700 mb-1">Username:</label>
                    <input v-model="username" type="text" placeholder="Your username" @keyup.enter.prevent="handleSubmit()" class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent"/>
                </div>
                <div class="text-sm font-medium text-gray-700 mb-5">
                    <label class="block text-sm font-medium text-gray-700 mb-1">Password:</label>
                    <input v-model="password" type="password" placeholder="••••••••" @keyup.enter.prevent="handleSubmit()" class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent"/>
                </div>
                <button v-if="isLogin" type="submit" class="w-full bg-green-600 hover:bg-green-700 text-white font-medium px-4 py-2 rounded-lg">Sign In</button>
                <button v-else type="submit" class="w-full bg-green-600 hover:bg-green-700 text-white font-medium px-4 py-2 rounded-lg">Register</button>
            </form>
            <p class="text-center text-green-800 mt-4" @click="isLogin=!isLogin">{{ isLogin ? "Don't have an account? Sign up" : "Already have an account? Sign in"}}</p>
        </div>       
    </div>
</template>
<style scoped>
</style>