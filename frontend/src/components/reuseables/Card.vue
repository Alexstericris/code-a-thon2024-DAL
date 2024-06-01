<script setup>
import {defineProps} from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faXmark} from "@fortawesome/free-solid-svg-icons";

const props = defineProps(
    {
      hideCorner: Boolean,
      hideFooter: Boolean
    });
</script>

<template>
  <div class="card">
    <div class="card-header">
<!--      <div v-if="!hideCorner" class="card-corner">-->
<!--        <slot name="right-corner">-->
<!--          <button>-->
<!--            <FontAwesomeIcon :icon="faXmark"></FontAwesomeIcon>-->
<!--          </button>-->

<!--        </slot>-->
<!--      </div>-->
      <div class="card-title">
        <slot name="title">Default title</slot>
        <slot v-if="!hideCorner" name="right-corner">
          <button>
            <FontAwesomeIcon :icon="faXmark"></FontAwesomeIcon>
          </button>
        </slot>
      </div>
      <div class="card-subtitle">
        <slot name="subtitle">Default subtitle</slot>
      </div>
    </div>
    <div class="card-body">
      <div class="card-text">
        <slot name="text">Default text</slot>
      </div>
    </div>
    <div v-if="!props.hideFooter" class="card-footer">
      <slot name="footer">Default footer</slot>
    </div>
  </div>
</template>

<style scoped>

</style>