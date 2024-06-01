import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useGlobalStore = defineStore('global', () => {
    const backgroundImg = ref('wind.jpg')

    return {backgroundImg}
})
