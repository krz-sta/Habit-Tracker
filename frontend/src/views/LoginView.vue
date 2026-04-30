<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')
const error = ref<string | null>(null)

async function handleLogin() {
    error.value = null
    try {
        await authStore.login(username.value, password.value)
        router.push('/home')
    } catch (e: any) {
        error.value = e.response?.data?.detail ?? 'Login failed.'
    }
}
</script>

<template>
    <div class="bg-green-100">
        <h1>Login</h1>
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button @click="handleLogin">Login</button>
        <p v-if="error">{{ error }}</p>
    </div>
</template>
<style scoped>
</style>