package com.astra.fintrack.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Data
@NoArgsConstructor
@Entity
public class StockHolding {
    @Id
    @GeneratedValue
    private Long id;

    private String symbol;          // e.g., AAPL, TSLA
    private int quantity;
    private double buyPrice;
    private LocalDate buyDate;
    private double currentPrice;

    // Getters, setters, etc.
}