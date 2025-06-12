package com.astra.fintrack.crons;

import com.astra.fintrack.dtos.StockTickerResponse;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Optional;

@Service
public class PolygonStockService {

    private static final String API_KEY = "Aoox5JzfEKlal5apcr_SpFp22yhqVcW_";
    private static final String BASE_URL = "https://api.polygon.io/v3/reference/tickers";

    private final RestTemplate restTemplate;

    public PolygonStockService(RestTemplateBuilder builder) {
        this.restTemplate = builder.build();
    }

    public Optional<StockTickerResponse.Result> fetchStock(String symbol) {
        String url = BASE_URL + "?ticker=" + symbol + "&market=stocks&active=true&apiKey=" + API_KEY;

        try {
            StockTickerResponse response = restTemplate.getForObject(url, StockTickerResponse.class);
            if (response != null && response.getResults() != null && !response.getResults().isEmpty()) {
                return Optional.of(response.getResults().getFirst());
            }
        } catch (Exception e) {
            System.err.println("Error fetching stock data: " + e.getMessage());
        }

        return Optional.empty();
    }
}
