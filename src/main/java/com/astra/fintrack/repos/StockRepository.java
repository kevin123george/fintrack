package com.astra.fintrack.repos;

import com.astra.fintrack.model.StockHolding;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StockRepository extends JpaRepository<StockHolding, Long> {
}
