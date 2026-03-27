package se.hegardt.dto

import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.PartialDate

import java.time.LocalDate

@Serdeable
class PartialDateDto {
    Integer day
    Integer month
    Integer year
    LocalDate date

    static PartialDateDto from(PartialDate date) {
        if (!date) return new PartialDateDto()
        new PartialDateDto(
            day: date.day,
            month: date.month,
            year: date.year,
            date: date.date
        )
    }
}
