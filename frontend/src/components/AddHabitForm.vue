<script setup lang="ts">
const { type } = defineProps<{
    type: string
}>()

import { useHabitStore } from '@/stores/habits';
import { useToastStore } from '@/stores/toast';
import { Plus } from 'lucide-vue-next';
import { ref, computed } from 'vue';

const name = ref<string>('');
const desc = ref<string>('');
const isExpanded = ref<boolean>(false);

const habitStore = useHabitStore();
const toastStore = useToastStore();

async function handleSubmit() {
    if (!name.value.trim()) {
        toastStore.show('Habit name is required.')
        return
    }
    if (name.value.length > 100) {
        toastStore.show('Habit name should be shorter than 100 characters.')
        return
    }
    await habitStore.createHabit(name.value, desc.value, type)
    name.value = ''
    desc.value = ''
    isExpanded.value = false
}

</script>

<template>
<button
    v-if="!isExpanded"
    @click="isExpanded = true"
    :class="`w-full p-4 rounded-lg border-2 border-dashed transition-colors ${
        type === 'good'
            ? 'border-green-300 hover:bg-green-50 hover:border-green-400'
            : 'border-red-300 hover:bg-red-50 hover:border-red-400'
    }`"
>
    <div class="flex items-center justify-center gap-2">
        <Plus class="w-5 h-5" />
        <span>Add a {{ type }} habit</span>
    </div>
</button>

<form v-else @submit.prevent="handleSubmit()" :class="`p-4 rounded-lg border-2 ${
    type === 'good'
      ? 'bg-green-50 border-green-200'
      : 'bg-red-50 border-red-200'}`
    ">
    <input
        type="text"
        v-model="name"
        placeholder="Habit Name"
        class="w-full px-3 py-2 rounded-md border border-gray-300 mb-2"
    />
    <textarea
        v-model="desc"
        placeholder="Description (optional)"
        class="w-full px-3 py-2 rounded-md border border-gray-300 mb-2"
        rows="2"
    />
    <div class="flex gap-2">
        <button type="submit" :class="`flex-1 px-4 py-2 rounded-md text-white ${
            type === 'good'
                ? 'bg-green-600 hover:bg-green-700'
                : 'bg-red-600 hover:bg-red-700'
            }`"
        >
            Add Habit
        </button>
        <button
            type="button"
            @click="name=''; desc=''; isExpanded=false"
            :class="`px-4 py-2 rounded-md bg-white border border-gray-300 hover:bg-gray-50`"
        >
            Cancel
        </button>
    </div>
</form>
</template>

<style scoped></style>