package com.astra.fintrack.dtos;

import lombok.Data;

import java.util.List;

@Data
public class StockTickerResponse {
    private List<Result> results;
    private String status;
    @Data
    public static class Result {
        private String ticker;
        private String name;
        private String market;
        private String currency_name;

        // Getters & setters
    }

    // Getters & setters
}