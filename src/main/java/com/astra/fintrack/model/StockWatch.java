package com.astra.fintrack.model;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;
import java.util.List;

@Entity
@Data
public class StockWatch {

    @Id
    private String symbol;

    private double initialPrice;

    private double currentPrice;

    private LocalDateTime addedAt = LocalDateTime.now();

    @OneToMany(mappedBy = "stock", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    private List<StockPriceEntry> priceHistory;



}
