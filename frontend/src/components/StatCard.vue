<script setup lang="ts">
defineProps<{
    label: string
    value: any
    bgColor: string
}>()
</script>

<template>
<div :class="[bgColor, 'rounded-lg p-4']">
    <div class="flex items-center gap-2 mb-2">
        <slot name="icon" />
    </div>
    <div class="text-2xl font-bold text-gray-900">{{ value }}</div>
    <div class="text-sm text-gray-600">{{ label }}</div>
</div>
</template>

<style scoped>
</style>