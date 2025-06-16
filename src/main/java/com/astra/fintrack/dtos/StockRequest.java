package com.astra.fintrack.dtos;

import java.time.LocalDate;

public class StockRequest {
    public String symbol;
    public double quantity;
    public double buyPrice;
    public LocalDate buyDate;
    public double currentPrice;
}
