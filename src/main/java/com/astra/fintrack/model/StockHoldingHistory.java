package com.astra.fintrack.model;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@Entity
public class StockHoldingHistory {
    @Id
    @GeneratedValue
    private Long id;

    private Long stockHoldingId;
    private String symbol;
    private double quantity;
    private double buyPrice;
    private LocalDate buyDate;
    private double currentPrice;
    private LocalDateTime updatedAt;
}