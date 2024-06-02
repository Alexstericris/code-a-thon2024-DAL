<script setup>
import {defineProps} from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faUpRightAndDownLeftFromCenter, faXmark} from "@fortawesome/free-solid-svg-icons";

const props = defineProps(
    {
      hideCorner: Boolean,
      hideFooter: Boolean,
      hideSubtitle: Boolean,
      hideText: Boolean,
      hideBody: Boolean
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
          <FontAwesomeIcon class="link-box"
                         :icon="faXmark"></FontAwesomeIcon>
        </slot>
      </div>
      <div v-if="!hideSubtitle" class="card-subtitle">
        <slot name="subtitle">Default subtitle</slot>
      </div>
    </div>
    <div v-if="!hideBody" class="card-body">
      <div v-if="!hideText" class="card-text">
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