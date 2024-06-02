import {ref, computed} from 'vue'
import {defineStore} from 'pinia'

export const useGlobalStore = defineStore('global', () => {
    const backgroundImg = ref('wind.jpg')
    const viewContract=ref(null)
    const viewAsset=ref(null)
    const viewInvoice=ref(null)
    return {backgroundImg,viewContract,viewAsset,viewInvoice}
})
