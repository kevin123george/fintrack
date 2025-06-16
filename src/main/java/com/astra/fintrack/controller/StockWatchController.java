package com.astra.fintrack.controller;

import com.astra.fintrack.model.StockWatch;
import com.astra.fintrack.services.StockWatchService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/stocks-watch")
public class StockWatchController {


    private final StockWatchService stockWatchService;

    public StockWatchController(StockWatchService stockWatchService) {
        this.stockWatchService = stockWatchService;
    }

    @PostMapping
    public String addStock(@RequestBody StockWatch request) {
        return stockWatchService.addToWatchlist(request);
    }

    @GetMapping
    public List<StockWatch> getAllStocks() {
        return stockWatchService.getAllStocks();
    }

}
