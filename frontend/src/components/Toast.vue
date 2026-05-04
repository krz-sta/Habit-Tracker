<script setup lang="ts">
import { useToastStore } from '@/stores/toast'
const toastStore = useToastStore()
</script>

<template>
    <div
        v-if="toastStore.message"
        class="fixed top-12 left-1/2 -translate-x-1/2 px-5 py-3 rounded-lg shadow-lg bg-white text-red-600 text-sm font-semibold border border-gray-300"
    >
        {{ toastStore.message }}
    </div>
</template>