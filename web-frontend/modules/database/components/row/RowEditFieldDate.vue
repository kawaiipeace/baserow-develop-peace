<template>
  <div class="control__elements">
    <div class="field-date__container">
      <div class="input__with-icon field-date">
        <input
          ref="date"
          v-model="date"
          type="text"
          class="input"
          :class="{ 'input--error': touched && !valid }"
          :placeholder="getDatePlaceholder(field)"
          :disabled="readOnly"
          @keyup.enter="$refs.date.blur()"
          @keyup="updateDate(field, date)"
          @focus="focus($refs.dateContext, $event)"
          @blur="blur($refs.dateContext, $event)"
        />
        <i class="iconoir-calendar"></i>
        <Context
          ref="dateContext"
          :hide-on-click-outside="false"
          class="datepicker-context"
        >
          <client-only>
            <date-picker
              v-if="!readOnly"
              :inline="true"
              :monday-first="true"
              :use-utc="true"
              :value="pickerDate"
              :language="datePickerLang[$i18n.locale]"
              class="datepicker"
              @input="chooseDate(field, $event)"
            ></date-picker>
          </client-only>
        </Context>
      </div>
      <div
        v-if="field.date_include_time"
        class="input__with-icon field-date__time"
      >
        <input
          ref="time"
          v-model="time"
          type="text"
          class="input"
          :class="{ 'input--error': touched && !valid }"
          :placeholder="getTimePlaceholder(field)"
          :disabled="readOnly"
          @keyup.enter="$refs.time.blur()"
          @keyup="updateTime(field, time)"
          @focus="focus($refs.timeContext, $event)"
          @blur="blur($refs.timeContext, $event)"
        />
        <i class="iconoir-clock"></i>
        <TimeSelectContext
          v-if="!readOnly"
          ref="timeContext"
          :value="time"
          :hide-on-click-outside="false"
          :notation="field.date_time_format"
          @input="chooseTime(field, $event)"
        ></TimeSelectContext>
      </div>
      <div class="field-date__tzinfo">
        {{ getCellTimezoneAbbr(field, value, { force: true }) }}
      </div>
    </div>
    <div v-show="touched && !valid" class="error">
      {{ error }}
    </div>
  </div>
</template>

<script>
import TimeSelectContext from '@baserow/modules/core/components/TimeSelectContext'
import rowEditField from '@baserow/modules/database/mixins/rowEditField'
import rowEditFieldInput from '@baserow/modules/database/mixins/rowEditFieldInput'
import dateField from '@baserow/modules/database/mixins/dateField'
import { en, fr } from 'vuejs-datepicker/dist/locale'

export default {
  components: { TimeSelectContext },
  mixins: [rowEditField, rowEditFieldInput, dateField],
  data() {
    return {
      datePickerLang: {
        en,
        fr,
      },
    }
  },
  methods: {
    focus(...args) {
      this.select()
      dateField.methods.focus.call(this, ...args)
    },
    blur(...args) {
      dateField.methods.blur.call(this, ...args)
      this.unselect()
    },
  },
}
</script>
