import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useAuthStore = defineStore('auth', () => {
    const authUser = ref(null)

    return {authUser}
})
