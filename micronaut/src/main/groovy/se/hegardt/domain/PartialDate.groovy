package se.hegardt.domain

import groovy.transform.CompileStatic
import jakarta.annotation.Nullable
import jakarta.persistence.Column
import jakarta.persistence.Embeddable
import jakarta.persistence.PrePersist
import jakarta.persistence.PreUpdate

import java.time.LocalDate

@Embeddable
@CompileStatic
class PartialDate {

    @Column(name = 'partial_day')
    @Nullable
    Integer day

    @Column(name = 'partial_month')
    @Nullable
    Integer month

    @Column(name = 'partial_year')
    @Nullable
    Integer year

    @Column(name = 'partial_date')
    @Nullable
    LocalDate date

    @PrePersist
    @PreUpdate
    void computeDate() {
        if (!year) {
            date = null
            return
        }
        date = LocalDate.of(year, month ?: 1, day ?: 1)
    }
}
